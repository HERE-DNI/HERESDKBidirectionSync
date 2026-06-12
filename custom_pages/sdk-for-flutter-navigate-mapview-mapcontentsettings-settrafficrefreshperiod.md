---
title: "setTrafficRefreshPeriod static method"
slug: "sdk-for-flutter-navigate-mapview-mapcontentsettings-settrafficrefreshperiod"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setTrafficRefreshPeriod.html -->


<div>
<h1>setTrafficRefreshPeriod static method</h1></div>

void
setTrafficRefreshPeriod(<ol class="parameter-list single-line"> <li>Duration value</li>
</ol>)

      

    

<p>Sets the traffic data refresh period for both <a href="/sdk-for-flutter-navigate-mapview-mapfeatures-trafficflow">MapFeatures.trafficFlow</a> and
<a href="/sdk-for-flutter-navigate-mapview-mapfeatures-trafficincidents">MapFeatures.trafficIncidents</a>.</p>
<p>By default, the traffic information
validity time and the refresh period is derived from the refresh period of HERE's traffic server.
The period set by this function will override the server's default setting for
upcoming traffic data requests.
Defaults to 60 seconds.</p>
<ul>
<li><code>value</code> Traffic data refresh period in seconds. Valid range is [60, 300] seconds.
The shortest refresh period that can be set is 60 seconds. This means that the traffic
data shown on a map view will be refreshed every minute.
The longest refresh period that can be set is 300 seconds. This means that the traffic
data shown on the current map view will be refreshed every 5 minutes
if the viewport does not change.
Note that when a viewport change occurs, new traffic data may be requested
regardless of the set refresh period. For example, during turn-by-turn navigation,
frequent viewport changes can result in missing traffic data, causing new requests
to be made more often.</li>
</ul>
<p>Throws <a href="/sdk-for-flutter-navigate-mapview-mapcontentsettingstrafficrefreshperiodexceptionexception-class">MapContentSettingsTrafficRefreshPeriodExceptionException</a>. <a href="/sdk-for-flutter-navigate-mapview-mapcontentsettingstrafficrefreshperiodexceptionexception-class">MapContentSettingsTrafficRefreshPeriodExceptionException</a> indicates what went wrong.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static void setTrafficRefreshPeriod(Duration value) =&gt; $prototype.setTrafficRefreshPeriod(value);</code></pre>

 



</div>
`
}</HTMLBlock>
