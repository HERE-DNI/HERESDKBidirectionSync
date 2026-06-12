---
title: "toDiagnosticsNode method"
slug: "sdk-for-flutter-explore-mapview-heremap-todiagnosticsnode"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- toDiagnosticsNode.html -->


<div>
<h1>toDiagnosticsNode method</h1></div>

<div>
<ol class="annotation-list">
<li>@override</li>
</ol>
</div>
DiagnosticsNode
toDiagnosticsNode({<ol class="parameter-list"> <li>String? name, </li>
<li>DiagnosticsTreeStyle? style, </li>
</ol>})

      <div class="features">inherited</div>


<p>Returns a debug representation of the object that is used by debugging
tools and by <code>DiagnosticsNode.toStringDeep</code>.</p>
<p>Leave <code>name</code> as null if there is not a meaningful description of the
relationship between the this node and its parent.</p>
<p>Typically the <code>style</code> argument is only specified to indicate an atypical
relationship between the parent and the node. For example, pass
<code>DiagnosticsTreeStyle.offstage</code> to indicate that a node is offstage.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@override
DiagnosticsNode toDiagnosticsNode({String? name, DiagnosticsTreeStyle? style}) {
  return DiagnosticableTreeNode(name: name, value: this, style: style);
}</code></pre>

 



</div>
`
}</HTMLBlock>
