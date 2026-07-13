---
title: "authenticateWithSDKNativeEngine method - Authentication class - core library - Dart API"
slug: "sdk-for-flutter-navigate-core-authentication-authenticatewithsdknativeengine"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core/Authentication-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">authenticateWithSDKNativeEngine</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-authenticationdata-class">AuthenticationData</a></span> <span class="name">authenticateWithSDKNativeEngine</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-authenticateWithSDKNativeEngine-param-sdkNativeEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkNativeEngine</span></span>

)

</div>

<div class="section desc markdown">

Uses the authentication service that is connected to the given SDK engine to authenticate and retrieve a secure token.

This method operates synchronously.

- `sdkNativeEngine` The SDK engine instance.

Returns <a href="sdk-for-flutter-navigate-core-authenticationdata-class">AuthenticationData</a>. Authentication data.

Throws <a href="sdk-for-flutter-navigate-core-authenticationexceptionexception-class">AuthenticationExceptionException</a>. Authentication exception that describes the error.

</div>

## Implementation

``` dart
static AuthenticationData authenticateWithSDKNativeEngine(SDKNativeEngine sdkNativeEngine) => $prototype.authenticateWithSDKNativeEngine(sdkNativeEngine);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

