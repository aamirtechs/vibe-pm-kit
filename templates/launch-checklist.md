# Launch checklist

## Product
- [ ] The v1 slice works end to end for a brand new user with no help
- [ ] Empty states, error states, and loading states are written, not blank
- [ ] No placeholder copy, dead buttons, or sample data in production
- [ ] Prices, limits, and terms shown to users match reality

## AI behaviour
- [ ] Eval scorecard filled in for the shipped model and prompt versions
- [ ] The model cannot leak system prompts, keys, or other users' data
- [ ] Failure mode tested: bad input, huge input, abusive input
- [ ] Cost per user estimated at 10x expected traffic

## Data and privacy
- [ ] Only the data the feature needs is collected and stored
- [ ] Anything used for training or tuning has a dataset card
- [ ] Delete and export paths exist for user data

## Support and operations
- [ ] A human can see what the AI did for a user (logs or admin view)
- [ ] Rollback plan written down and tested once
- [ ] One page of help or FAQ answers the five likeliest questions

## Growth
- [ ] README or landing page states the problem in the user's own words
- [ ] One screenshot or short demo clip shows the payoff, not the settings
- [ ] Launch post drafted for one community where the users already are
