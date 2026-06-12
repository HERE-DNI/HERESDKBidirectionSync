---
title: "getRealisticViewWarning abstract method"
slug: "sdk-for-flutter-navigate-warner-warningsregistry-getrealisticviewwarning"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getRealisticViewWarning.html -->


<div>
<h1>getRealisticViewWarning abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-navigation-realisticviewwarning-class">RealisticViewWarning</a>?
getRealisticViewWarning(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-warner-warning-class">Warning</a> warning</li>
</ol>)

      

    

<p>Returns a realistic-view warning corresponding to the given identifier.</p>
<ul>
<li><code>warning</code> The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
The <code>warning</code> uniquely identifies a single realistic-view warning within this registry
and is used to retrieve its full metadata.</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-navigation-realisticviewwarning-class">RealisticViewWarning?</a>. The <a href="/sdk-for-flutter-navigate-navigation-realisticviewwarning-class">RealisticViewWarning</a> object associated with the provided <code>WarningsRegistry.getRealisticViewWarning.warning</code>,
or <code>null</code> if no warning exists for the given <code>WarningsRegistry.getRealisticViewWarning.warning</code>.
This object contains the full details and attributes of the corresponding warning.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">RealisticViewWarning? getRealisticViewWarning(Warning warning);</code></pre>

 



</div>
`
}</HTMLBlock>
