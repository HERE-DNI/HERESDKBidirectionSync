---
title: "TimeRule constructor - TimeRule - core library - Dart API"
slug: "sdk-for-flutter-navigate-core-timerule-timerule"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core/TimeRule-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">TimeRule</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">TimeRule</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-timeRule" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">timeRule</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-timeZoneOffsetSeconds" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">timeZoneOffsetSeconds</span>, </span>
3.  <span id="sdk-for-flutter-navigate-param-dstSpec" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">dstSpec</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance of this class.

- `timeRule` The time rule as a string in ISO 14825 format.

- `timeZoneOffsetSeconds` The time zone offset in seconds for the location where the time rule applies.

- `dstSpec` Day saving time specification, as a string in ISO 14825 format, for the location where the time rule applies.

</div>

## Implementation

``` dart
factory TimeRule(String timeRule, int timeZoneOffsetSeconds, String dstSpec) => $prototype.make(timeRule, timeZoneOffsetSeconds, dstSpec);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

