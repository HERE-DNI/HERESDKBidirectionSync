---
title: "getRoadSignWarning abstract method"
slug: "sdk-for-flutter-navigate-warner-warningsregistry-getroadsignwarning"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getRoadSignWarning.html -->


<div>
<h1>getRoadSignWarning abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-navigation-roadsignwarning-class">RoadSignWarning</a>?
getRoadSignWarning(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-warner-warning-class">Warning</a> warning</li>
</ol>)

      

    

<p>Returns a road-sign warning corresponding to the given identifier.</p>
<ul>
<li><code>warning</code> The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
The <code>warning</code> uniquely identifies a single road sign warning within this registry
and is used to retrieve its full metadata.</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-navigation-roadsignwarning-class">RoadSignWarning?</a>. The <code>sdk.navigation.RoadSignWarning</code> object associated with the provided <code>WarningsRegistry.getRoadSignWarning.warning</code>,
or <code>null</code> if no warning exists for the given <code>WarningsRegistry.getRoadSignWarning.warning</code>.
This object contains the full details and attributes of the corresponding warning.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">RoadSignWarning? getRoadSignWarning(Warning warning);</code></pre>

 



</div>
`
}</HTMLBlock>
