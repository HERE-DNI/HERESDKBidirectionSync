---
title: "deserialize method - Route class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-route-deserialize"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- deserialize.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/Route-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">deserialize</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-routing-route-class">Route</a>?</span> <span class="name">deserialize</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-deserialize-param-routeData" class="parameter"><span class="type-annotation">Uint8List</span> <span class="parameter-name">routeData</span></span>

)

</div>

<div class="section desc markdown">

Creates route from the given binary data.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

- `routeData` The binary of a serialized route.

Returns <a href="sdk-for-flutter-navigate-routing-route-class">Route?</a>. The route object restored from the binary data.

</div>

## Implementation

``` dart
static Route? deserialize(Uint8List routeData) => $prototype.deserialize(routeData);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
