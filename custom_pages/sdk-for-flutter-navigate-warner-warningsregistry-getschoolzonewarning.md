---
title: "getSchoolZoneWarning abstract method"
slug: "sdk-for-flutter-navigate-warner-warningsregistry-getschoolzonewarning"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getSchoolZoneWarning.html -->


<div>
<h1>getSchoolZoneWarning abstract method</h1></div>

<a href="sdk-for-flutter-navigate-navigation-schoolzonewarning-class">SchoolZoneWarning</a>?
getSchoolZoneWarning(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-warner-warning-class">Warning</a> warning</li>
</ol>)

      

    

<p>Returns a school zone warning corresponding to the given identifier.</p>
<ul>
<li><code>warning</code> The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
The <code>warning</code> uniquely identifies a single school zone warning within this registry
and is used to retrieve its full metadata.</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-navigation-schoolzonewarning-class">SchoolZoneWarning?</a>. The <a href="sdk-for-flutter-navigate-navigation-schoolzonewarning-class">SchoolZoneWarning</a> object associated with the provided <code>WarningsRegistry.getSchoolZoneWarning.warning</code>,
or <code>null</code> if no warning exists for the given <code>WarningsRegistry.getSchoolZoneWarning.warning</code>.
This object contains the full details and attributes of the corresponding warning.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">SchoolZoneWarning? getSchoolZoneWarning(Warning warning);</code></pre>

 



</div>
`
}</HTMLBlock>
