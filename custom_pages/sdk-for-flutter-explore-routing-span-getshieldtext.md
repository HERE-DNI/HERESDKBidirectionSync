---
title: "getShieldText abstract method"
slug: "sdk-for-flutter-explore-routing-span-getshieldtext"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getShieldText.html -->


<div>
<h1>getShieldText abstract method</h1></div>

String
getShieldText(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-routing-localizedroadnumber-class">LocalizedRoadNumber</a> roadNumber</li>
</ol>)

      

    

<p>Converts full route number to the value to be displayed on the road shield.</p>
<p>The results are based on country code and state code of <code>Span</code> object and route type of passed <code>road_number</code> argument.</p>
<ul>
<li><code>roadNumber</code> Route number to convert to shield text.</li>
</ul>
<p>Returns <code>String</code>. Text on the road shield to display.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">String getShieldText(LocalizedRoadNumber roadNumber);</code></pre>

 



</div>
`
}</HTMLBlock>
