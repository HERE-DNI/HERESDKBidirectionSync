---
title: "occupantsNumber property"
slug: "sdk-for-flutter-explore-routing-busoptions-occupantsnumber"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- occupantsNumber.html -->


<div>
<h1>occupantsNumber property</h1></div>

        
        int
        occupantsNumber
<div class="features">getter/setter pair</div>


<p>Specifies the number of occupants in the vehicle, including driver,
can affect the vehicle's ability to use HOV/carpool restricted lanes.
Shouldn't be less than 1 or greater than 255. Defaults to 1.</p>
<p><strong>Note:</strong> This parameter has no effect unless HOV and/or HOT lane usage is enabled via <a href="/sdk-for-flutter-explore-routing-busoptions-allowoptions">BusOptions.allowOptions</a> and such lanes are available in the selected country.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int occupantsNumber;</code></pre>

 



</div>
`
}</HTMLBlock>
