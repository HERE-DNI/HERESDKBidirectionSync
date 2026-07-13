---
title: "customEngineOptions property - SDKOptions class - core.engine library - Dart API"
slug: "sdk-for-flutter-navigate-core.engine-sdkoptions-customengineoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- customEngineOptions.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/SDKOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">customEngineOptions</span> property

</div>

<div class="section multi-line-signature">

Map<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-engine-enginebaseurl">EngineBaseURL</a></span>, <span class="type-parameter"><a href="sdk-for-flutter-navigate-core-engine-engineoptions-class">EngineOptions</a></span>\></span> <span class="name">customEngineOptions</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Set custom options for SDK Engines. This includes:

- `custom_base_url`: Allows engines to use custom base URLs for alternative services. By default, the available endpoints use HERE backend endpoints. If unsupported base URLs are specified, the related features will become non-functional. Please contact your HERE representative to learn about possible custom base URL usage options.
- `custom_authentication_mode`: Enables bearer authentication mode for engines, which adds or omits the header ("Authorization", "Bearer \$Token") to each online request made by the module the object is added to. The token (if used) can be provided directly or retrieved via key/secret from a dedicated backend. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
Map<EngineBaseURL, EngineOptions> customEngineOptions;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
