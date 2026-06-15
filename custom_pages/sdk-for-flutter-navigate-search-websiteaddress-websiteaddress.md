---
title: "WebsiteAddress constructor"
slug: "sdk-for-flutter-navigate-search-websiteaddress-websiteaddress"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- WebsiteAddress.html -->


<div>
<h1>WebsiteAddress constructor</h1></div>

WebsiteAddress(<ol class="parameter-list single-line"> <li>String address, </li>
<li>List&lt;<a href="sdk-for-flutter-navigate-search-placecategory-class">PlaceCategory</a>&gt; categories</li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>address</code> The website address.</li>
<li><code>categories</code> Categories associated with website address.
Note: In case <a href="sdk-for-flutter-navigate-search-websiteaddress-categories">WebsiteAddress.categories</a> are not empty, then <a href="sdk-for-flutter-navigate-search-websiteaddress-address">WebsiteAddress.address</a> should be used according to given categories.
Otherwise, <a href="sdk-for-flutter-navigate-search-websiteaddress-address">WebsiteAddress.address</a> is meant for general use.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">WebsiteAddress(this.address, this.categories);</code></pre>

 



</div>
`
}</HTMLBlock>
