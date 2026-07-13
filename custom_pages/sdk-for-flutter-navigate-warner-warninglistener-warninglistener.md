---
title: "WarningListener constructor - WarningListener - warner library - Dart API"
slug: "sdk-for-flutter-navigate-warner-warninglistener-warninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- WarningListener.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="warner/WarningListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">WarningListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">WarningListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onWarningsLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onWarningsLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-warner-warning-class">Warning</a></span>\></span></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

A generic listener interface abstract class for receiving warning notifications.

Implementations of this interface are notified whenever the `WarnerEngine` detects new warnings. The listener receives a list of `Warning` objects, each describing a specific event or condition that requires user attention.

Classes interested in warning updates should implement this listener and register themselves via `WarnerEngine.addWarningListener`.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
factory WarningListener(
  void Function(List<Warning>) onWarningsLambda,

) => WarningListener$Lambdas(
  onWarningsLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
