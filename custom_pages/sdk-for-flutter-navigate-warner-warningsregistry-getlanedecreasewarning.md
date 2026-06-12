---
title: "getLaneDecreaseWarning abstract method"
slug: "sdk-for-flutter-navigate-warner-warningsregistry-getlanedecreasewarning"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getLaneDecreaseWarning.html -->


<div>
<h1>getLaneDecreaseWarning abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-warner-lanedecreasewarning-class">LaneDecreaseWarning</a>?
getLaneDecreaseWarning(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-warner-warning-class">Warning</a> warning</li>
</ol>)

      

    

<p>Returns a lane decrease warning corresponding to the given identifier.</p>
<ul>
<li><code>warning</code> The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
The <code>warning</code> uniquely identifies a single lane decrease warning within this registry
and is used to retrieve its full metadata.</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-warner-lanedecreasewarning-class">LaneDecreaseWarning?</a>. The <code>LaneDecreaseWarning</code> object associated with the provided <code>WarningsRegistry.getLaneDecreaseWarning.warning</code>,
or <code>null</code> if no warning exists for the given <code>WarningsRegistry.getLaneDecreaseWarning.warning</code>.
This object contains the full details and attributes of the corresponding warning.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LaneDecreaseWarning? getLaneDecreaseWarning(Warning warning);</code></pre>

 



</div>
`
}</HTMLBlock>
