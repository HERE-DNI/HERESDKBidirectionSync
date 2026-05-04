---
title: "TrafficFlowBase (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttrafficflowbase"
hidden: false
---

Package [com.here.sdk.traffic](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface TrafficFlowBase

All Known Implementing Classes:
[`TrafficFlow`](sdk-for-android-explore-api-reference-latesttrafficflow "class in com.here.sdk.traffic")

------------------------------------------------------------------------
public interface TrafficFlowBase
This interface provides details about a traffic flow.
For additional information about fields, refer to [Traffic API v7 API Reference: Traffic API v7](https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic).

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `double`

  [getFreeFlowSpeedInMetersPerSecond](#getFreeFlowSpeedInMetersPerSecond())`()`

Gets the reference speed in meters per second along the roadway when no traffic is present.

`double`

  [getJamFactor](#getJamFactor())`()`

Gets a value for the amount of traffic on the roadway.

## Method Details

### getFreeFlowSpeedInMetersPerSecond

double getFreeFlowSpeedInMetersPerSecond()

    Gets the reference speed in meters per second along the roadway when no traffic is present.
Returns:
    The reference speed in meters per second along the roadway when no traffic is present.

### getJamFactor

double getJamFactor()

    Gets a value for the amount of traffic on the roadway.

    The value, between 0.0 and 10.0, indicate the expected quality of travel. A value of 0.0 indicates that there is no congestion on the roadway. As the value approaches 10.0, it indicates increasing congestion. A value of 10.0 is reserved to represent a blocked roadway (closure).
Returns:
    A value for the amount of traffic on the roadway.
