---
title: "getType method - Metadata class - core library - Dart API"
slug: "sdk-for-flutter-explore-core-metadata-gettype"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getType.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core/Metadata-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getType</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-core-metadatatype">MetadataType</a>?</span> <span class="name">getType</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-getType-param-key" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">key</span></span>

)

</div>

<div class="section desc markdown">

Determines the type of a metadata value.

If the type of a metadata value associated with a key is not known, this method will enable the type to be queried, in order to know which get method to call. i.e. getDouble(), getInteger() etc.

- `key` The name of the key for which to obtain the type.

Returns <a href="sdk-for-flutter-explore-core-metadatatype">MetadataType?</a>. An enumeration describing the type of the value associated with the key.

</div>

## Implementation

``` dart
MetadataType? getType(String key);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
