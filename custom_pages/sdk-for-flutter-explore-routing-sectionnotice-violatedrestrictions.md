---
title: "violatedRestrictions property"
slug: "sdk-for-flutter-explore-routing-sectionnotice-violatedrestrictions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- violatedRestrictions.html -->


<div>
<h1>violatedRestrictions property</h1></div>

        
        List&lt;<a href="/sdk-for-flutter-explore-routing-violatedrestriction-class">ViolatedRestriction</a>&gt;
violatedRestrictions
<div class="features">getter/setter pair</div>


<p>The following property <code>violated_restrictions</code> contains the notice detail information.
Only three types of restrictions can have notice details: time dependent restriction, vehicle restriction and transport mode restriction.
There is no one-to-one match of the <code>SectionNotice.code</code> and these three restriction types. For example, if <code>SectionNotice.code</code> is
<a href="/sdk-for-flutter-explore-routing-sectionnoticecode">SectionNoticeCode.violatedVehicleRestriction</a>, then it can be either vehicle restriction or transport mode restriction. If <code>SectionNotice.code</code> is
<a href="/sdk-for-flutter-explore-routing-sectionnoticecode">SectionNoticeCode.seasonalClosure</a>, then it is time dependent restriction.
If the section notice is none of the above-mentioned three types, then this will be an empty list.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;ViolatedRestriction&gt; violatedRestrictions;</code></pre>

 



</div>
`
}</HTMLBlock>
