---
title: "enableUsageStats method - SDKNativeEngine class - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core-engine-sdknativeengine-enableusagestats"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/SDKNativeEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">enableUsageStats</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">enableUsageStats</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-enableUsageStats-param-enabled" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">enabled</span></span>

)

</div>

<div class="section desc markdown">

Enable or disable <a href="sdk-for-flutter-explore-core-engine-usagestats-class">UsageStats</a> for the HERE SDK.

Defaults to disabled (false). When enabled,

    SDKNativeEngine.getSdkUsageStats()

returns actual online data consumption. Note that the flag does not cancel pending requests. <a href="sdk-for-flutter-explore-core-engine-usagestats-class">UsageStats</a> can be enabled or disabled at any time.
</p>

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

- `enabled` True, if UsageStats are enabled.

</div>

## Implementation

``` dart
void enableUsageStats(bool enabled);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

