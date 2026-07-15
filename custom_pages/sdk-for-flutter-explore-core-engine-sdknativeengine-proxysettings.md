---
title: "proxySettings property - SDKNativeEngine class - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core-engine-sdknativeengine-proxysettings"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/SDKNativeEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">proxySettings</span> property

</div>

<div id="sdk-for-flutter-explore-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-core-engine-proxysettings-class">ProxySettings</a>?</span> <span class="name">proxySettings</span>

</div>

<div class="section desc markdown">

Proxy settings of this SDK engine that will be used by HERE SDK network for all requests. Defaults to (`null`), which indicates proxy is not enabled. When setting proxy settings, they will immediately be applied and all the pending and fresh requests will use these settings. Pass (`null`) to indicate that proxy should be disabled. If proxy is necessary from the start then it's recommended to use <a href="sdk-for-flutter-explore-core-engine-networksettings-proxysettings">NetworkSettings.proxySettings</a> in <a href="sdk-for-flutter-explore-core-engine-sdkoptions-networksettings">SDKOptions.networkSettings</a>.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process. Gets the current proxy settings.

</div>

## Implementation

``` dart
ProxySettings? get proxySettings;
```

</div>

<div id="sdk-for-flutter-explore-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">proxySettings=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-proxySettings-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-engine-proxysettings-class">ProxySettings</a>?</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

Proxy settings of this SDK engine that will be used by HERE SDK network for all requests. Defaults to (`null`), which indicates proxy is not enabled. When setting proxy settings, they will immediately be applied and all the pending and fresh requests will use these settings. Pass (`null`) to indicate that proxy should be disabled. If proxy is necessary from the start then it's recommended to use <a href="sdk-for-flutter-explore-core-engine-networksettings-proxysettings">NetworkSettings.proxySettings</a> in <a href="sdk-for-flutter-explore-core-engine-sdkoptions-networksettings">SDKOptions.networkSettings</a>.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process. Sets the proxy settings.

</div>

## Implementation

``` dart
set proxySettings(ProxySettings? value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

