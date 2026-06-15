---
title: "addLocationIssueListener method"
slug: "sdk-for-flutter-navigate-location-locationengine-addlocationissuelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- addLocationIssueListener.html -->


<div>
<h1>addLocationIssueListener method</h1></div>

void
addLocationIssueListener(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-location-locationissuelistener-class">LocationIssueListener</a> listener</li>
</ol>)

      <div class="features">override</div>


<p>Adds a <a href="sdk-for-flutter-navigate-location-locationissuelistener-class">LocationIssueListener</a> to the engine to get notified when a location issue has occurred
Supports more than one listener, instance is added only once.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void addLocationIssueListener(LocationIssueListener listener) {
  if (!_locationIssueListeners.containsKey(listener)) {
    _locationIssueListeners[listener] = LocationIssueListenerBridge(listener);
  }
  _location.addLocationIssueListener(_locationIssueListeners[listener]!);
}</code></pre>

 



</div>
`
}</HTMLBlock>
