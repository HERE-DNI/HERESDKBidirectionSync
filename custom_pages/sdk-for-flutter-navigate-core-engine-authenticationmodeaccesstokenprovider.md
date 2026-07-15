---
title: "AuthenticationModeAccessTokenProvider typedef - core.engine library - Dart API"
slug: "sdk-for-flutter-navigate-core-engine-authenticationmodeaccesstokenprovider"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">AuthenticationModeAccessTokenProvider</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">AuthenticationModeAccessTokenProvider</span> = <span class="returntype">String? Function<span class="signature">()</span></span>

</div>

<div class="section desc markdown">

This lambda is used to retrieve access token in synchronous manner.

It returns the access token or null if it is not set. The lambda is called each time the access token is needed and it is executed on the main thread of the application.

Returns Access token in case it is set or null otherwise.

</div>

## Implementation

``` dart
typedef AuthenticationModeAccessTokenProvider = String? Function();
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

