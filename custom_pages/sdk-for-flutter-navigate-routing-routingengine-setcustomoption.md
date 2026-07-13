---
title: "setCustomOption method - RoutingEngine class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-routingengine-setcustomoption"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/RoutingEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setCustomOption</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-routing-routingerror">RoutingError</a>?</span> <span class="name">setCustomOption</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setCustomOption-param-name" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">name</span>, </span>
2.  <span id="sdk-for-flutter-navigate-setCustomOption-param-value" class="parameter"><span class="type-annotation">String?</span> <span class="parameter-name">value</span></span>

)

</div>

<div class="section desc markdown">

Sets a custom option for routing backend queries.

The custom option is applied to all the queries that `RoutingEngine` performs. For a complete list of available parameter names and their valid values, refer to <a href="https://www.here.com/docs/bundle/routing-api-v8-api-reference/page/index.html">HERE Routing API v8</a>. **Note:** It's easy to set a wrong option that makes queries invalid, so make sure you read and understand the backend documentation.

- `name` An option name. If the engine already has an option with the same name, the option will be overwritten. The option name must be a non-empty string.

- `value` An option value. If the value is `null`, the option will be removed. The option value must be a non-empty string.

Returns <a href="sdk-for-flutter-navigate-routing-routingerror">RoutingError?</a>. An optional error of setting the option.

It's `null` if the option has been set successfully. It's `RoutingError.INVALID_PARAMETER` if the input name and/or value haven't passed internal validation.

</div>

## Implementation

``` dart
RoutingError? setCustomOption(String name, String? value);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

