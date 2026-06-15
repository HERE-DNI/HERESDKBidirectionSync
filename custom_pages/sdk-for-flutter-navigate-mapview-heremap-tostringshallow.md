---
title: "toStringShallow method"
slug: "sdk-for-flutter-navigate-mapview-heremap-tostringshallow"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- toStringShallow.html -->


<div>
<h1>toStringShallow method</h1></div>

String
toStringShallow({<ol class="parameter-list"> <li>String joiner = ', ', </li>
<li>DiagnosticLevel minLevel = DiagnosticLevel.debug, </li>
</ol>})

      <div class="features">inherited</div>


<p>Returns a one-line detailed description of the object.</p>
<p>This description is often somewhat long. This includes the same
information given by <code>toStringDeep</code>, but does not recurse to any children.</p>
<p><code>joiner</code> specifies the string which is place between each part obtained
from <code>debugFillProperties</code>. Passing a string such as <code>'\n '</code> will result
in a multiline string that indents the properties of the object below its
name (as per <code>toString</code>).</p>
<p><code>minLevel</code> specifies the minimum <code>DiagnosticLevel</code> for properties included
in the output.</p>
<p>See also:</p>
<ul>
<li><code>toString</code>, for a brief description of the object.</li>
<li><code>toStringDeep</code>, for a description of the subtree rooted at this object.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">String toStringShallow({String joiner = ', ', DiagnosticLevel minLevel = DiagnosticLevel.debug}) {
  String? shallowString;
  assert(() {
    final StringBuffer result = StringBuffer();
    result.write(toString());
    result.write(joiner);
    final DiagnosticPropertiesBuilder builder = DiagnosticPropertiesBuilder();
    debugFillProperties(builder);
    result.write(
      builder.properties.where((DiagnosticsNode n) =&gt; !n.isFiltered(minLevel)).join(joiner),
    );
    shallowString = result.toString();
    return true;
  }());
  return shallowString ?? toString();
}</code></pre>

 



</div>
`
}</HTMLBlock>
