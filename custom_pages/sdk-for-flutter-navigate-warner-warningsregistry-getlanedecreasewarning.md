---
title: "getLaneDecreaseWarning method - WarningsRegistry class - warner library - Dart API"
slug: "sdk-for-flutter-navigate-warner-warningsregistry-getlanedecreasewarning"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="warner/WarningsRegistry-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getLaneDecreaseWarning</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-warner-lanedecreasewarning-class">LaneDecreaseWarning</a>?</span> <span class="name">getLaneDecreaseWarning</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-getLaneDecreaseWarning-param-warning" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-warner-warning-class">Warning</a></span> <span class="parameter-name">warning</span></span>

)

</div>

<div class="section desc markdown">

Returns a lane decrease warning corresponding to the given identifier.

- `warning` The identifier of the warning, as provided by `WarningListener.onWarning`. The `warning` uniquely identifies a single lane decrease warning within this registry and is used to retrieve its full metadata.

Returns <a href="sdk-for-flutter-navigate-warner-lanedecreasewarning-class">LaneDecreaseWarning?</a>. The `LaneDecreaseWarning` object associated with the provided `WarningsRegistry.getLaneDecreaseWarning.warning`, or `null` if no warning exists for the given `WarningsRegistry.getLaneDecreaseWarning.warning`. This object contains the full details and attributes of the corresponding warning.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
LaneDecreaseWarning? getLaneDecreaseWarning(Warning warning);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

