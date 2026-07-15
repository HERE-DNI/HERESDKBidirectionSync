---
title: "customAuthenticationMode property - EngineOptions class - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core-engine-engineoptions-customauthenticationmode"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/EngineOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">customAuthenticationMode</span> property

</div>

<div class="section multi-line-signature">

<a href="sdk-for-flutter-explore-core-engine-authenticationmode-class">AuthenticationMode</a>? <span class="name">customAuthenticationMode</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Allows bearer authentication mode for engines. This mode adds a header ("Authorization", "Bearer \$Token") to each online request made by the module the object is added to. The token can either be provided directly or retrieved via key/secret from a dedicated backend.

</div>

## Implementation

``` dart
AuthenticationMode? customAuthenticationMode;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

