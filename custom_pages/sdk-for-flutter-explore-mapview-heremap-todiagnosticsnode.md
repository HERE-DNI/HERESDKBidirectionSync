---
title: "toDiagnosticsNode method - HereMap class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-heremap-todiagnosticsnode"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- toDiagnosticsNode.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/HereMap-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">toDiagnosticsNode</span> method

</div>

<div class="section multi-line-signature">

<div>

1.  @override

</div>

<span class="returntype">DiagnosticsNode</span> <span class="name">toDiagnosticsNode</span>(<wbr></wbr>{

1.  <span id="sdk-for-flutter-explore-toDiagnosticsNode-param-name" class="parameter"><span class="type-annotation">String?</span> <span class="parameter-name">name</span>, </span>
2.  <span id="sdk-for-flutter-explore-toDiagnosticsNode-param-style" class="parameter"><span class="type-annotation">DiagnosticsTreeStyle?</span> <span class="parameter-name">style</span>, </span>

})

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<div class="section desc markdown">

Returns a debug representation of the object that is used by debugging tools and by `DiagnosticsNode.toStringDeep`.

Leave `name` as null if there is not a meaningful description of the relationship between the this node and its parent.

Typically the `style` argument is only specified to indicate an atypical relationship between the parent and the node. For example, pass `DiagnosticsTreeStyle.offstage` to indicate that a node is offstage.

</div>

## Implementation

``` dart
@override
DiagnosticsNode toDiagnosticsNode({String? name, DiagnosticsTreeStyle? style}) {
  return DiagnosticableTreeNode(name: name, value: this, style: style);
}
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
