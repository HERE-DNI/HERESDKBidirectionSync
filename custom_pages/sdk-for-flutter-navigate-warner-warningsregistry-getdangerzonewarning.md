---
title: "getDangerZoneWarning abstract method"
slug: "sdk-for-flutter-navigate-warner-warningsregistry-getdangerzonewarning"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getDangerZoneWarning.html -->


<div>
<h1>getDangerZoneWarning abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-navigation-dangerzonewarning-class">DangerZoneWarning</a>?
getDangerZoneWarning(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-warner-warning-class">Warning</a> warning</li>
</ol>)

      

    

<p>Returns a danger zone warning corresponding to the given identifier.</p>
<ul>
<li><code>warning</code> The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
The <code>warning</code> uniquely identifies a single danger zone warning within this registry
and is used to retrieve its full metadata.</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-navigation-dangerzonewarning-class">DangerZoneWarning?</a>. The <a href="/sdk-for-flutter-navigate-navigation-dangerzonewarning-class">DangerZoneWarning</a> object associated with the provided <code>WarningsRegistry.getDangerZoneWarning.warning</code>,
or <code>null</code> if no warning exists for the given <code>WarningsRegistry.getDangerZoneWarning.warning</code>.
This object contains the full details and attributes of the corresponding warning.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">DangerZoneWarning? getDangerZoneWarning(Warning warning);</code></pre>

 



</div>
`
}</HTMLBlock>
