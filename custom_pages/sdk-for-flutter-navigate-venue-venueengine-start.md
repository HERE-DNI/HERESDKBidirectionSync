---
title: "start abstract method"
slug: "sdk-for-flutter-navigate-venue-venueengine-start"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- start.html -->


<div>
<h1>start abstract method</h1></div>

void
start(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-authenticationcallback">AuthenticationCallback</a>? callback</li>
</ol>)

      

    

<p>Authenticates asynchronously using HERE SDK credentials and uses a result token to start
the <a href="sdk-for-flutter-navigate-venue-service-venueservice-class">VenueService</a>.</p>
<p>An initialization status of the venue service is
returned to objects registered as <a href="sdk-for-flutter-navigate-venue-service-venueservicelistener-class">VenueServiceListener</a>. If the
authentication will fail, the venue service will not be started.</p>
<ul>
<li><code>callback</code> The optional callback that will be triggered when the authentication will be completed.
If the authentication fails, the venue service will not be started.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void start(AuthenticationCallback? callback);</code></pre>

 



</div>
`
}</HTMLBlock>
