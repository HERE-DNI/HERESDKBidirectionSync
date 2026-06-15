---
title: "getCustomWarning abstract method"
slug: "sdk-for-flutter-navigate-warner-warningsregistry-getcustomwarning"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getCustomWarning.html -->


<div>
<h1>getCustomWarning abstract method</h1></div>

<a href="sdk-for-flutter-navigate-warner-customwarning-class">CustomWarning</a>?
getCustomWarning(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-warner-warning-class">Warning</a> warning</li>
</ol>)

      

    

<p>Returns additional data associated with the given custom warning.</p>
<p>The provided <code>WarningsRegistry.getCustomWarning.warning</code> identifies a specific custom warning instance by its
base warning information and custom warning type. This information is used
to resolve the corresponding entry in the warning registry and retrieve
any additional, type-specific data associated with the warning.</p>
<ul>
<li><code>warning</code> The <a href="sdk-for-flutter-navigate-warner-warning-class">Warning</a> instance identifying the custom warning for which
additional data should be retrieved.</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-warner-customwarning-class">CustomWarning?</a>. The <code>CustomWarning</code> associated with the given <code>WarningsRegistry.getCustomWarning.warning</code>, or <code>null</code>
if no additional data exists for this warning.
The returned object contains the payload with type-specific
details and attributes of the corresponding warning.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">CustomWarning? getCustomWarning(Warning warning);</code></pre>

 



</div>
`
}</HTMLBlock>
