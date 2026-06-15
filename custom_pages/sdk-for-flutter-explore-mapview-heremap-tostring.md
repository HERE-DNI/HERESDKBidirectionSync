---
title: "toString method"
slug: "sdk-for-flutter-explore-mapview-heremap-tostring"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- toString.html -->


<div>
<h1>toString method</h1></div>

<div>
<ol class="annotation-list">
<li>@override</li>
</ol>
</div>
String
toString({<ol class="parameter-list"> <li>DiagnosticLevel minLevel = DiagnosticLevel.info, </li>
</ol>})

      <div class="features">inherited</div>


<p>A string representation of this object.</p>
<p>Some classes have a default textual representation,
often paired with a static <code>parse</code> function (like <code>int.parse</code>).
These classes will provide the textual representation as
their string representation.</p>
<p>Other classes have no meaningful textual representation
that a program will care about.
Such classes will typically override <code>toString</code> to provide
useful information when inspecting the object,
mainly for debugging or logging.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@override
String toString({DiagnosticLevel minLevel = DiagnosticLevel.info}) {
  String? fullString;
  assert(() {
    fullString = toDiagnosticsNode(
      style: DiagnosticsTreeStyle.singleLine,
    ).toString(minLevel: minLevel);
    return true;
  }());
  return fullString ?? toStringShort();
}</code></pre>

 



</div>
`
}</HTMLBlock>
