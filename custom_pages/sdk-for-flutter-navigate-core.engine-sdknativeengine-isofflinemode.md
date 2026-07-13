---
title: "isOfflineMode property - SDKNativeEngine class - core.engine library - Dart API"
slug: "sdk-for-flutter-navigate-core.engine-sdknativeengine-isofflinemode"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/SDKNativeEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">isOfflineMode</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">bool</span> <span class="name">isOfflineMode</span>

</div>

<div class="section desc markdown">

The offline mode. Sets offline mode for the HERE SDK to offline or online. Defaults to false, which means the HERE SDK uses an online connection. When enabled, this prevents the HERE SDK from initiating any online connection except for provided pass through features if set. See <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-passthroughfeatures">SDKNativeEngine.passThroughFeatures</a>. Note that the flag does not cancel pending requests. The mode can be enabled or disabled at any time. In order to fully operate offline, the mode needs to be enabled via <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-offlinemode">SDKOptions.offlineMode</a>. Initialization of the HERE SDK itself does not require an internet connection. Returns `true` if the HERE SDK uses offline connection mode, otherwise returns `false`.

Note: This is a **beta** release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process. Gets the current offline mode.

</div>

## Implementation

``` dart
bool get isOfflineMode;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">isOfflineMode=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-isOfflineMode-param-value" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

The offline mode. Sets offline mode for the HERE SDK to offline or online. Defaults to false, which means the HERE SDK uses an online connection. When enabled, this prevents the HERE SDK from initiating any online connection except for provided pass through features if set. See <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-passthroughfeatures">SDKNativeEngine.passThroughFeatures</a>. Note that the flag does not cancel pending requests. The mode can be enabled or disabled at any time. In order to fully operate offline, the mode needs to be enabled via <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-offlinemode">SDKOptions.offlineMode</a>. Initialization of the HERE SDK itself does not require an internet connection. Returns `true` if the HERE SDK uses offline connection mode, otherwise returns `false`.

Note: This is a **beta** release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process. Sets the offline mode.

</div>

## Implementation

``` dart
set isOfflineMode(bool value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

