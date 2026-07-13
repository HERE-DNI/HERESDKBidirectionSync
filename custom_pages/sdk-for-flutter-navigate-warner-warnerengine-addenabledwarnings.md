---
title: "addEnabledWarnings method - WarnerEngine class - warner library - Dart API"
slug: "sdk-for-flutter-navigate-warner-warnerengine-addenabledwarnings"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- addEnabledWarnings.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="warner/WarnerEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">addEnabledWarnings</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">addEnabledWarnings</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-addEnabledWarnings-param-warningTypes" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a></span>\></span></span> <span class="parameter-name">warningTypes</span></span>

)

</div>

<div class="section desc markdown">

Adds the given warning types to the set of warnings monitored by the engine.

After this call, the engine will begin generating warnings for all types included in `WarnerEngine.addEnabledWarnings.warningTypes`, in addition to those that are already enabled.

- `warningTypes` Warning types to be added to the engine's active monitoring set.

</div>

## Implementation

``` dart
void addEnabledWarnings(List<WarningType> warningTypes);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
