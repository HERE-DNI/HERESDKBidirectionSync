---
title: "highDensityEncodingEnabled property - SearchOptions class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-searchoptions-highdensityencodingenabled"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/SearchOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">highDensityEncodingEnabled</span> property

</div>

<div class="section multi-line-signature">

bool <span class="name">highDensityEncodingEnabled</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Allows enabling high density encoding of relevant parameters. For now, it only affects input parameters of type `GeoCorridor`. Only supported for search in `SearchEngine`, otherwise it is ignored. **Note:** This is a closed-alpha release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process. Only participants of the closed-alpha group can get access from HERE to use this feature, otherwise, a <a href="sdk-for-flutter-navigate-search-searcherror">SearchError.forbidden</a> will be propagated in callbacks.

</div>

## Implementation

``` dart
bool highDensityEncodingEnabled;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

