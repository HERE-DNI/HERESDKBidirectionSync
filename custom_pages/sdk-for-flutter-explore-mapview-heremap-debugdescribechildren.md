---
title: "debugDescribeChildren method"
slug: "sdk-for-flutter-explore-mapview-heremap-debugdescribechildren"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- debugDescribeChildren.html -->


<div>
<h1>debugDescribeChildren method</h1></div>

<div>
<ol class="annotation-list">
<li>@<a href="https://pub.dev/documentation/meta/1.17.0/meta/protected-constant.html">protected</a></li>
</ol>
</div>
List&lt;DiagnosticsNode&gt;
debugDescribeChildren()

      <div class="features">inherited</div>


<p>Returns a list of <code>DiagnosticsNode</code> objects describing this node's
children.</p>
<p>Children that are offstage should be added with <code>style</code> set to
<code>DiagnosticsTreeStyle.offstage</code> to indicate that they are offstage.</p>
<p>The list must not contain any null entries. If there are explicit null
children to report, consider <code>DiagnosticsNode.message</code> or
<code>DiagnosticsProperty&lt;Object&gt;</code> as possible <code>DiagnosticsNode</code> objects to
provide.</p>
<p>Used by <code>toStringDeep</code>, <code>toDiagnosticsNode</code> and <code>toStringShallow</code>.</p>
<p>See also:</p>
<ul>
<li><code>RenderTable.debugDescribeChildren</code>, which provides high quality custom
descriptions for its child nodes.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@protected
List&lt;DiagnosticsNode&gt; debugDescribeChildren() =&gt; const &lt;DiagnosticsNode&gt;[];</code></pre>

 



</div>
`
}</HTMLBlock>
