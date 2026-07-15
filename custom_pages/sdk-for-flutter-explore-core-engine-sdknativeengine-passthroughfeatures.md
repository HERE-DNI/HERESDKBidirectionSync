---
title: "passThroughFeatures property - SDKNativeEngine class - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core-engine-sdknativeengine-passthroughfeatures"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/SDKNativeEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">passThroughFeatures</span> property

</div>

<div id="sdk-for-flutter-explore-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">Set<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-engine-passthroughfeature">PassThroughFeature</a></span>\></span>?</span> <span class="name">passThroughFeatures</span>

</div>

<div class="section desc markdown">

The pass through features. Sets pass through features which are allowed to use online data when HERE SDK is in offline mode. Pass through features can be updated at any time. When offline mode is disabled, existing pass through features will be removed. These needs to be set again when you enable offline mode next time. By default, reporting of HERE SDK <a href="sdk-for-flutter-explore-core-engine-usagestats-class">UsageStats</a> will be enabled when at least one pass-through feature is set.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process. Gets the pass through features.

</div>

## Implementation

``` dart
Set<PassThroughFeature>? get passThroughFeatures;
```

</div>

<div id="sdk-for-flutter-explore-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">passThroughFeatures=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-passThroughFeatures-param-value" class="parameter"><span class="type-annotation">Set<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-engine-passthroughfeature">PassThroughFeature</a></span>\></span>?</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

The pass through features. Sets pass through features which are allowed to use online data when HERE SDK is in offline mode. Pass through features can be updated at any time. When offline mode is disabled, existing pass through features will be removed. These needs to be set again when you enable offline mode next time. By default, reporting of HERE SDK <a href="sdk-for-flutter-explore-core-engine-usagestats-class">UsageStats</a> will be enabled when at least one pass-through feature is set.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process. Sets the pass through features.

</div>

## Implementation

``` dart
set passThroughFeatures(Set<PassThroughFeature>? value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

