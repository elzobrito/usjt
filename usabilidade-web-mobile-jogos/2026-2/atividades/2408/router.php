<?php

namespace OliviaRouter;

class Router
{
    /**
     * @var array
     */
    private $route = [];
    private $clausules = [];

    public function get($pattern, $controller_method)
    {
        $this->route('get', $pattern, $controller_method, isset($this->clausules['middleware']) ? $this->clausules['middleware'] : null);
    }

    public function requestPost($dado)
    {
        return filter_input(INPUT_POST, $dado);
    }

    public function post($pattern, $controller_method)
    {
        if ($_SESSION['CSRF'] === true) {
            if ($this->requestPost('_token') == $_SESSION['UUID'])
                $this->route('post', $pattern, $controller_method, isset($this->clausules['middleware']) ? $this->clausules['middleware'] : null);
        } else {
            $this->route('post', $pattern, $controller_method, isset($this->clausules['middleware']) ? $this->clausules['middleware'] : null);
        }
    }

    public function route($http_method, $pattern, $controller_method, $middleware)
    {
        $pattern = $this->route_to_regex('/' . $_SESSION['BASENAME'] . $pattern);
        $this->route[$http_method . $pattern] = [
            'http_method' => $http_method,
            'url_pattern' => $pattern,
            'controller_method' => $controller_method,
            'middleware' => $middleware
        ];
    }

    private function route_to_regex($path)
    {
        $slashes_escaped = str_replace('/', '\/', $path);
        $route = preg_replace_callback('/({:.+?})/', function ($matches) {
            $param_name = preg_replace("/[^A-Za-z0-9 ]/", '', $matches[0]);
            return "(?<{$param_name}>.*)";
        }, $slashes_escaped);
        return '/^' . $route . '$/';
    }

    private function call_middleware_class($str)
    {
        $callables = explode('#', $str);
        $controller = [];

        foreach (explode('/', $callables[0]) as $controller_part)
            array_push($controller, ucfirst($controller_part));

        $controller = $_SESSION['App_folder'] . '\\' . $_SESSION['Middleware_folder'] . '\\' . implode('\\', $controller);

        return ['middleware' => $controller, 'action' => $callables[1]];
    }

    private function call_controller_class($str)
    {
        $callables = explode('#', $str);
        $controller = [];

        foreach (explode('/', $callables[0]) as $controller_part)
            array_push($controller, ucfirst($controller_part));

        $controller = $_SESSION['App_folder'] . '\\' . $_SESSION['Controller_folder'] . '\\' . implode('\\', $controller);

        return ['controller' => $controller, 'action' => $callables[1]];
    }

    public function execute($request_data)
    {
        $_SESSION['e404'] = true;
        foreach ($this->route as $pattern => $actions) {
            if ($request_data['REQUEST_METHOD'] === strtoupper($actions['http_method'])) {
                if (preg_match($actions['url_pattern'], $request_data['REQUEST_URI'], $params) === 1) {
                    $callables = $this->call_controller_class($actions['controller_method']);

                    $controller = new $callables['controller'];
                    $format = array_key_exists('CONTENT_TYPE', $request_data) ? $request_data['CONTENT_TYPE'] : 'text/html';
                    $params['format'] = explode('/', $format)[1];
                    $params['method'] = $request_data['REQUEST_METHOD'];

                    if ($actions['middleware'] != null) {
                        $call_middleware = $this->call_middleware_class($actions['middleware'] . '#index');
                        $middle = new $call_middleware['middleware'];
                        $middle->{$call_middleware['action']}();
                    }

                    $controller->{$callables['action']}($params);
                    $_SESSION['e404'] = false;
                    break;
                }
            }
        }
    }

    function __call($name, $arguments)
    {
        $clausule = $arguments[0];
        if (count($arguments) > 1)
            $clausule = $arguments;
        $this->clausules[strtolower($name)] = $clausule;
        return $this;
    }
}
