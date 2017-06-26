export KOPS_STATE_STORE=s3://kub-wavetesting-com-state-store
kops create -f https://raw.githubusercontent.com/Twark/kubernetes-tutorial/master/kops/mycluster2.wavetesting.com/cluster_config
kops create -f https://raw.githubusercontent.com/Twark/kubernetes-tutorial/master/kops/mycluster2.wavetesting.com/master_config
kops create -f https://raw.githubusercontent.com/Twark/kubernetes-tutorial/master/kops/mycluster2.wavetesting.com/nodes_config
kops create secret --name mycluster2.wavetesting.com sshpublickey admin -i ~/.ssh/id_rsa.pub
