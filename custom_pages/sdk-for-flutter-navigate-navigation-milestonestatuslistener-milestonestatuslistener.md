---
title: "MilestoneStatusListener constructor"
slug: "sdk-for-flutter-navigate-navigation-milestonestatuslistener-milestonestatuslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MilestoneStatusListener.html -->


<div>
<h1>MilestoneStatusListener constructor</h1></div>

MilestoneStatusListener(<ol class="parameter-list single-line"> <li>void onMilestoneStatusUpdatedLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-navigation-milestone-class">Milestone</a>, </li>
<li><a href="/sdk-for-flutter-navigate-navigation-milestonestatus">MilestoneStatus</a></li>
</ol>)</li>
</ol>)
    

<p>This abstract class should be
implemented in order to receive notifications from this class about the
arrival at each <a href="/sdk-for-flutter-navigate-navigation-milestone-class">Milestone</a> or missing it.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MilestoneStatusListener(
  void Function(Milestone, MilestoneStatus) onMilestoneStatusUpdatedLambda,

) =&gt; MilestoneStatusListener$Lambdas(
  onMilestoneStatusUpdatedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
