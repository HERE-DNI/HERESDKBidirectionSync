---
title: "freeResource method - MapContext class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcontext-freeresource"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- freeResource.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapContext-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">freeResource</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">freeResource</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-freeResource-param-type" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapcontextresourcetype">MapContextResourceType</a></span> <span class="parameter-name">type</span>, </span>
2.  <span id="sdk-for-flutter-explore-freeResource-param-severity" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapcontextfreeresourceseverity">MapContextFreeResourceSeverity</a></span> <span class="parameter-name">severity</span></span>

)

</div>

<div class="section desc markdown">

Frees a system resource held by the <a href="sdk-for-flutter-explore-mapview-mapcontext-class">MapContext</a> and all entities attached to it, like <a href="sdk-for-flutter-explore-mapview-heremapcontrollercore-class">HereMapControllerCore</a>.

This function is intended for use when a system resource availability becomes low. For example, some memory can be freed when the application transitions to the background state.

- `type` Type of resource to be freed.

- `severity` Severity of the request.

</div>

## Implementation

``` dart
void freeResource(MapContextResourceType type, MapContextFreeResourceSeverity severity);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
