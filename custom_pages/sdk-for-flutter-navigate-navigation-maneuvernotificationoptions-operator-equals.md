---
title: "operator == method"
slug: "sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-operator-equals"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- operator_equals.html -->


<div>
<h1>operator == method</h1></div>

<div>
<ol class="annotation-list">
<li>@override</li>
</ol>
</div>
bool
operator ==(<ol class="parameter-list single-line"> <li>Object other</li>
</ol>)

      

    

<p>The equality operator.</p>
<p>The default behavior for all <code>Object</code>s is to return true if and
only if this object and <code>other</code> are the same object.</p>
<p>Override this method to specify a different equality relation on
a class. The overriding method must still be an equivalence relation.
That is, it must be:</p>
<ul>
<li>
<p>Total: It must return a boolean for all arguments. It should never throw.</p>
</li>
<li>
<p>Reflexive: For all objects <code>o</code>, <code>o == o</code> must be true.</p>
</li>
<li>
<p>Symmetric: For all objects <code>o1</code> and <code>o2</code>, <code>o1 == o2</code> and <code>o2 == o1</code> must
either both be true, or both be false.</p>
</li>
<li>
<p>Transitive: For all objects <code>o1</code>, <code>o2</code>, and <code>o3</code>, if <code>o1 == o2</code> and
<code>o2 == o3</code> are true, then <code>o1 == o3</code> must be true.</p>
</li>
</ul>
<p>The method should also be consistent over time,
so whether two objects are equal should only change
if at least one of the objects was modified.</p>
<p>If a subclass overrides the equality operator, it should override
the <a href="/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-hashcode">hashCode</a> method as well to maintain consistency.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@override
bool operator ==(Object other) {
  if (identical(this, other)) return true;
  if (other is! ManeuverNotificationOptions) return false;
  ManeuverNotificationOptions _other = other;
  return language == _other.language &amp;&amp;
      unitSystem == _other.unitSystem &amp;&amp;
      DeepCollectionEquality().equals(includedNotificationTypes, _other.includedNotificationTypes) &amp;&amp;
      enableRoundaboutNotification == _other.enableRoundaboutNotification &amp;&amp;
      enableDestinationReachedNotification == _other.enableDestinationReachedNotification &amp;&amp;
      arrivalNotificationOption == _other.arrivalNotificationOption &amp;&amp;
      enableDoubleNotification == _other.enableDoubleNotification &amp;&amp;
      enablePhoneme == _other.enablePhoneme &amp;&amp;
      notificationFormatOption == _other.notificationFormatOption &amp;&amp;
      textUsageOptions == _other.textUsageOptions &amp;&amp;
      enableHighwayExit == _other.enableHighwayExit &amp;&amp;
      enableLaneRecommendation == _other.enableLaneRecommendation &amp;&amp;
      DeepCollectionEquality().equals(includedNaturalGuidanceTypes, _other.includedNaturalGuidanceTypes) &amp;&amp;
      directionInformationUsageForActionNotificationOption == _other.directionInformationUsageForActionNotificationOption;
}</code></pre>

 



</div>
`
}</HTMLBlock>
