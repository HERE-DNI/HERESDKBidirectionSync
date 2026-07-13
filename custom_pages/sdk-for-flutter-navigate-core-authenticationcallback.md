---
title: "AuthenticationCallback typedef - core library - Dart API"
slug: "sdk-for-flutter-navigate-core-authenticationcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- AuthenticationCallback.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">AuthenticationCallback</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">AuthenticationCallback</span> = <span class="returntype">void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-authenticationError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-authenticationerror">AuthenticationError</a>?</span> <span class="parameter-name">authenticationError</span>, </span><span id="sdk-for-flutter-navigate-param-authenticationData" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-authenticationdata-class">AuthenticationData</a>?</span> <span class="parameter-name">authenticationData</span></span>)</span></span>

</div>

<div class="section desc markdown">

Callback passed to <a href="sdk-for-flutter-navigate-core-authentication-authenticatewithsdknativeengine">Authentication.authenticateWithSDKNativeEngine</a>.

This callback is called on the main thread asynchronously when an authenticate call has completed.

- `authenticationError` Represents the operation status. It is 'null' for an operation that succeeds.

- `authenticationData` Represents the authentication data.

</div>

## Implementation

``` dart
typedef AuthenticationCallback = void Function(AuthenticationError? authenticationError, AuthenticationData? authenticationData);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
