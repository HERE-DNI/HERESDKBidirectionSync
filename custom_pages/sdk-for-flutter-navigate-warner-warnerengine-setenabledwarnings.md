---
title: "setEnabledWarnings method - WarnerEngine class - warner library - Dart API"
slug: "sdk-for-flutter-navigate-warner-warnerengine-setenabledwarnings"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="warner/WarnerEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setEnabledWarnings</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">setEnabledWarnings</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setEnabledWarnings-param-warningTypes" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a></span>\></span></span> <span class="parameter-name">warningTypes</span></span>

)

</div>

<div class="section desc markdown">

Replaces the current set of enabled warning types with the provided list.

After this call, the engine will monitor and generate warnings only for types included in `WarnerEngine.setEnabledWarnings.warningTypes`.

- `warningTypes` The complete new set of warning types the engine should track.

</div>

## Implementation

``` dart
void setEnabledWarnings(List<WarningType> warningTypes);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

