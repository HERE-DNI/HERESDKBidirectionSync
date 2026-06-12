---
title: "removeLocationIssueListener method"
slug: "sdk-for-flutter-navigate-location-locationengine-removelocationissuelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- removeLocationIssueListener.html -->


<div>
<h1>removeLocationIssueListener method</h1></div>

void
removeLocationIssueListener(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-location-locationissuelistener-class">LocationIssueListener</a> listener</li>
</ol>)

      <div class="features">override</div>


<p>Removes a <a href="/sdk-for-flutter-navigate-location-locationissuelistener-class">LocationIssueListener</a> from the engine.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void removeLocationIssueListener(LocationIssueListener listener) {
  LocationIssueListenerBridge? bridge = _locationIssueListeners.remove(listener);
  if (bridge == null) {
    return;
  }
  _location.removeLocationIssueListener(bridge);
}</code></pre>

 



</div>
`
}</HTMLBlock>
