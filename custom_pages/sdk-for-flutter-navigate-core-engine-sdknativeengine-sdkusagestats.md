---
title: "sdkUsageStats property - SDKNativeEngine class - core.engine library - Dart API"
slug: "sdk-for-flutter-navigate-core-engine-sdknativeengine-sdkusagestats"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/SDKNativeEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">sdkUsageStats</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-engine-usagestats-class">UsageStats</a></span>\></span></span> <span class="name">sdkUsageStats</span>

</div>

<div class="section desc markdown">

Gets a list of usage statistics for all available HERE SDK features. <a href="sdk-for-flutter-navigate-core-engine-usagestats-class">UsageStats</a> has cache and persistent storage. Reads from the persistent storage happen on `SDKNativeEngine` creation step. Writes to persistent storage happen by reaching internal limit (amount of upload bytes, by default is 50KB).

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process. Gets a list of usage statistics for all available HERE SDK features.

</div>

## Implementation

``` dart
List<UsageStats> get sdkUsageStats;
```

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

