---
title: "getRailwayCrossingWarning abstract method"
slug: "sdk-for-flutter-navigate-warner-warningsregistry-getrailwaycrossingwarning"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getRailwayCrossingWarning.html -->


<div>
<h1>getRailwayCrossingWarning abstract method</h1></div>

<a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarning-class">RailwayCrossingWarning</a>?
getRailwayCrossingWarning(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-warner-warning-class">Warning</a> warning</li>
</ol>)

      

    

<p>Returns a railway crossing warning corresponding to the given identifier.</p>
<ul>
<li><code>warning</code> The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
The <code>warning</code> uniquely identifies a single railway crossing warning within this registry
and is used to retrieve its full metadata.</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarning-class">RailwayCrossingWarning?</a>. The <a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarning-class">RailwayCrossingWarning</a> object associated with the provided <code>WarningsRegistry.getRailwayCrossingWarning.warning</code>,
or <code>null</code> if no warning exists for the given <code>WarningsRegistry.getRailwayCrossingWarning.warning</code>.
This object contains the full details and attributes of the corresponding warning.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">RailwayCrossingWarning? getRailwayCrossingWarning(Warning warning);</code></pre>

 



</div>
`
}</HTMLBlock>
