---
title: "authenticate method - Authentication class - core library - Dart API"
slug: "sdk-for-flutter-navigate-core-authentication-authenticate"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- authenticate.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core/Authentication-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">authenticate</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">authenticate</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-authenticate-param-sdkNativeEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkNativeEngine</span>, </span>
2.  <span id="sdk-for-flutter-navigate-authenticate-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-authenticationcallback">AuthenticationCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Uses the authentication service that is connected to the given SDK engine to authenticate and retrieve a secure token.

This method operates asynchronously.

- `sdkNativeEngine` The SDK engine instance.

- `callback` Callback to retrieve an authentication token on the main thread.

</div>

## Implementation

``` dart
static void authenticate(SDKNativeEngine sdkNativeEngine, AuthenticationCallback callback) => $prototype.authenticate(sdkNativeEngine, callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
