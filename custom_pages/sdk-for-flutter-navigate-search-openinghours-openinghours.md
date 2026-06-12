---
title: "OpeningHours constructor"
slug: "sdk-for-flutter-navigate-search-openinghours-openinghours"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- OpeningHours.html -->


<div>
<h1>OpeningHours constructor</h1></div>

OpeningHours(<ol class="parameter-list"> <li>List&lt;String&gt; text, </li>
<li>bool isOpen, </li>
<li>List&lt;<a href="/sdk-for-flutter-navigate-search-scheduledetails-class">ScheduleDetails</a>&gt; scheduleDetailsList, </li>
<li>List&lt;<a href="/sdk-for-flutter-navigate-search-placecategory-class">PlaceCategory</a>&gt; categories, </li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>text</code> The list of opening hours presented as localized text.</li>
<li><code>isOpen</code> Boolean flag informing if the place is open or closed at the time when the search request was initiated.
For offline search, this is calculated using device's time,
so it may give incorrect value if device and place are located in different time zones.</li>
<li><code>scheduleDetailsList</code> The list of schedule details.</li>
<li><code>categories</code> The list of categories related to opening hours information.
This data is not available in offline search.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">OpeningHours(this.text, this.isOpen, this.scheduleDetailsList, this.categories);</code></pre>

 



</div>
`
}</HTMLBlock>
