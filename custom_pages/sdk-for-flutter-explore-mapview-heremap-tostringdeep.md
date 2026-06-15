---
title: "toStringDeep method"
slug: "sdk-for-flutter-explore-mapview-heremap-tostringdeep"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- toStringDeep.html -->


<div>
<h1>toStringDeep method</h1></div>

String
toStringDeep({<ol class="parameter-list"> <li>String prefixLineOne = '', </li>
<li>String? prefixOtherLines, </li>
<li>DiagnosticLevel minLevel = DiagnosticLevel.debug, </li>
<li>int wrapWidth = 65, </li>
</ol>})

      <div class="features">inherited</div>


<p>Returns a string representation of this node and its descendants.</p>
<p><code>prefixLineOne</code> will be added to the front of the first line of the
output. <code>prefixOtherLines</code> will be added to the front of each other line.
If <code>prefixOtherLines</code> is null, the <code>prefixLineOne</code> is used for every line.
By default, there is no prefix.</p>
<p><code>minLevel</code> specifies the minimum <code>DiagnosticLevel</code> for properties included
in the output.</p>
<p><code>wrapWidth</code> specifies the column number where word wrapping will be
applied.</p>
<p>The <code>toStringDeep</code> method takes other arguments, but those are intended
for internal use when recursing to the descendants, and so can be ignored.</p>
<p>See also:</p>
<ul>
<li><code>toString</code>, for a brief description of the object but not its children.</li>
<li><code>toStringShallow</code>, for a detailed description of the object but not its
children.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">String toStringDeep({
  String prefixLineOne = '',
  String? prefixOtherLines,
  DiagnosticLevel minLevel = DiagnosticLevel.debug,
  int wrapWidth = 65,
}) {
  return toDiagnosticsNode().toStringDeep(
    prefixLineOne: prefixLineOne,
    prefixOtherLines: prefixOtherLines,
    minLevel: minLevel,
    wrapWidth: wrapWidth,
  );
}</code></pre>

 



</div>
`
}</HTMLBlock>
