---
title: "getWarningsRegistry method - WarnerEngine class - warner library - Dart API"
slug: "sdk-for-flutter-navigate-warner-warnerengine-getwarningsregistry"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getWarningsRegistry.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="warner/WarnerEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getWarningsRegistry</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-warner-warningsregistry-class">WarningsRegistry</a></span> <span class="name">getWarningsRegistry</span>(<wbr></wbr>)

</div>

<div class="section desc markdown">

Returns the centralized access point for retrieving full metadata of any supported warning category (e.g., safety cameras, truck restrictions, etc.).

<a href="sdk-for-flutter-navigate-warner-warningsregistry-class">WarningsRegistry</a> class exposes getter methods, each returning the detailed warning object for the given identifier. Use this getter to look up complete warning information by its id, as provided through `WarningListener.onWarning`.

Returns <a href="sdk-for-flutter-navigate-warner-warningsregistry-class">WarningsRegistry</a>. The centralized <a href="sdk-for-flutter-navigate-warner-warningsregistry-class">WarningsRegistry</a> instance.

</div>

## Implementation

``` dart
WarningsRegistry getWarningsRegistry();
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
