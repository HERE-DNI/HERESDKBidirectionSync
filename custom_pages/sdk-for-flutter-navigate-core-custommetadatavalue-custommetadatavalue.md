---
title: "CustomMetadataValue constructor - CustomMetadataValue - core library - Dart API"
slug: "sdk-for-flutter-navigate-core-custommetadatavalue-custommetadatavalue"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CustomMetadataValue.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core/CustomMetadataValue-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">CustomMetadataValue</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">CustomMetadataValue</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-getTagLambda" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">getTagLambda</span>()</span>

)

</div>

<div class="section desc markdown">

Abstract class for storing arbitrary metadata types.

By implementing this abstract class, multiple object types can be stored as desired, simply by adding fields to the implementation that refer to those objects and then assigning an instance of the CustomMetadataValue derived class to a map item.

</div>

## Implementation

``` dart
factory CustomMetadataValue(
  String Function() getTagLambda,

) => CustomMetadataValue$Lambdas(
  getTagLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
