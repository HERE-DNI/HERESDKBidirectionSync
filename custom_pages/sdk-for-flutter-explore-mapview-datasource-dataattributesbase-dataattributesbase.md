---
title: "DataAttributesBase constructor - DataAttributesBase - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-explore-mapview-datasource-dataattributesbase-dataattributesbase"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/DataAttributesBase-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">DataAttributesBase</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">DataAttributesBase</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-getAttributeNamesLambda" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span> <span class="parameter-name">getAttributeNamesLambda</span>(), </span>
2.  <span id="sdk-for-flutter-explore-param-getValueTypeLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-dataattributevaluevaluetype">DataAttributeValueValueType</a>?</span> <span class="parameter-name">getValueTypeLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation">String</span></span>

    ), </span>
3.  <span id="sdk-for-flutter-explore-param-getAsStringLambda" class="parameter"><span class="type-annotation">String?</span> <span class="parameter-name">getAsStringLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation">String</span></span>

    ), </span>
4.  <span id="sdk-for-flutter-explore-param-getStringLambda" class="parameter"><span class="type-annotation">String?</span> <span class="parameter-name">getStringLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation">String</span></span>

    ), </span>
5.  <span id="sdk-for-flutter-explore-param-getInt64Lambda" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">getInt64Lambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation">String</span></span>

    ), </span>
6.  <span id="sdk-for-flutter-explore-param-getFloatLambda" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">getFloatLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation">String</span></span>

    ), </span>
7.  <span id="sdk-for-flutter-explore-param-getDoubleLambda" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">getDoubleLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation">String</span></span>

    ), </span>
8.  <span id="sdk-for-flutter-explore-param-getBooleanLambda" class="parameter"><span class="type-annotation">bool?</span> <span class="parameter-name">getBooleanLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation">String</span></span>

    ), </span>
9.  <span id="sdk-for-flutter-explore-param-getValueLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-dataattributevalue-class">DataAttributeValue</a>?</span> <span class="parameter-name">getValueLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation">String</span></span>

    ), </span>

)

</div>

<div class="section desc markdown">

Interface for a collection of data attributes.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
factory DataAttributesBase(
  List<String> Function() getAttributeNamesLambda,
  DataAttributeValueValueType? Function(String) getValueTypeLambda,
  String? Function(String) getAsStringLambda,
  String? Function(String) getStringLambda,
  int? Function(String) getInt64Lambda,
  double? Function(String) getFloatLambda,
  double? Function(String) getDoubleLambda,
  bool? Function(String) getBooleanLambda,
  DataAttributeValue? Function(String) getValueLambda,

) => DataAttributesBase$Lambdas(
  getAttributeNamesLambda,
  getValueTypeLambda,
  getAsStringLambda,
  getStringLambda,
  getInt64Lambda,
  getFloatLambda,
  getDoubleLambda,
  getBooleanLambda,
  getValueLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

