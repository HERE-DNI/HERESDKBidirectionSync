---
title: "startWithToken abstract method"
slug: "sdk-for-flutter-navigate-venue-venueengine-startwithtoken"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- startWithToken.html -->


<div>
<h1>startWithToken abstract method</h1></div>

void
startWithToken(<ol class="parameter-list single-line"> <li>String token</li>
</ol>)

      

    

<p>Authenticates asynchronously using HERE SDK credentials using a token to start
the <a href="sdk-for-flutter-navigate-venue-service-venueservice-class">VenueService</a>.</p>
<p>An initialization status of the venue service is
returned to objects registered as <a href="sdk-for-flutter-navigate-venue-service-venueservicelistener-class">VenueServiceListener</a>. If the
authentication will fail, the venue service will not be started.</p>
<ul>
<li><code>token</code> SDK project scope token to be used for authentication</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void startWithToken(String token);</code></pre>

 



</div>
`
}</HTMLBlock>
